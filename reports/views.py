from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User, Bug
from .forms import SignupForm, BugForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create user object, not saved yet
            user.set_password(form.cleaned_data["password1"])  # Hash the password
            user.save()  # Now save to DB
            login(request, user)  # Log them in
            return redirect("dashboard")  # Redirect after signup
        else:
            # If form isn't valid, show errors (or debug in terminal)
            print(form.errors)  # Debugging: see what's wrong
            # You can also re-render the signup page with the same form to show errors
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def dashboard(request):
    if request.user.role == "researcher":
        return researcher_dashboard(request)
    elif request.user.role == "company":
        return company_dashboard(request) 
    elif request.user.role == "admin":
        return admin_dashboard(request)
    
    else:
        return redirect("login")

@login_required
def researcher_dashboard(request):
    # Show only bugs reported by the current user (who is a researcher).
    user_bugs = Bug.objects.filter(reporter=request.user)
    return render(request, "reports/researcher_dashboard.html", {"user_bugs": user_bugs})

@login_required
def company_dashboard(request):
    # Show only bugs where the current user is the assigned company
    company_bugs = Bug.objects.filter(company=request.user)

    return render(request, "reports/company_dashboard.html", {"company_bugs": company_bugs})

@login_required
def admin_dashboard(request):
    if request.user.role != "admin":
        return redirect("dashboard")  # Prevent non-admins from accessing

    # Fetch all users and all bugs
    all_users = User.objects.all()
    all_bugs = Bug.objects.all()

    return render(request, "reports/admin_dashboard.html", {
        "all_users": all_users,
        "all_bugs": all_bugs
    })



@login_required
def create_bug(request):
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.reporter = request.user
            bug.save()
            return redirect("dashboard") 
    else:
        form = BugForm()
    return render(request, "reports/create_bug.html", {"form": form})

@login_required
def update_bug_status(request, bug_id, new_status):
    try:
        bug = Bug.objects.get(pk=bug_id, company=request.user)
    except Bug.DoesNotExist:
        return redirect("dashboard")

    valid_statuses = ["under_review", "accepted", "rejected", "resolved"]
    if new_status not in valid_statuses:
        return redirect("dashboard")

    bug.status = new_status
    bug.save()

    return redirect("dashboard")


@login_required
def toggle_user_active(request, user_id, activate):
    # Check if current user is admin
    if request.user.role != "admin":
        return redirect("dashboard")

    try:
        user_to_toggle = User.objects.get(pk=user_id)
        # Prevent banning self
        if user_to_toggle == request.user:
            return redirect("admin_dashboard")
    except User.DoesNotExist:
        return redirect("admin_dashboard")

    if activate == 1:
        user_to_toggle.is_active = True
    else:
        user_to_toggle.is_active = False
    user_to_toggle.save()

    return redirect("admin_dashboard")

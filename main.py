from pyscript import document

# predefined grade sets
grade7 = {"Alice Johnson", "Ben Carter", "Chloe Diaz", "David Kim"}
grade8 = {"Eva Martinez", "Frank Wu", "Grace Lee", "Henry Patel"}
grade9 = {"Ivy Nguyen", "Jack Robinson", "Kara Singh", "Liam Turner"}
grade10 = {"Mia Chen", "Noah Garcia", "Olivia Brown", "Peter Novak"}

# stores members added by user
added_members = set()

# accepts event argument passed by py-click
def result_checker(event=None):
    # get and format full name
    fname = document.getElementById('first_name').value.strip()
    lname = document.getElementById('last_name').value.strip()
    full = (fname + " " + lname).title().strip()

    # build set, ignore blank input
    new_member = set([full]) - {""}

    # accumulate new member
    global added_members
    added_members |= new_member

    # merge all sets
    master_set = grade7 | grade8 | grade9 | grade10 | added_members

    # prepare data
    members_list = sorted(master_set)
    total = len(master_set)

    # build output html
    output_html = f"""
    <div>
        <div><b>ALL MEMBERS ({total}):</b></div>
        <div>{', '.join(members_list)}</div>
        <div><b>TOTAL MEMBERS: {total}</b></div>
    </div>
    """

    # update output div
    document.getElementById('output').innerHTML = output_html

    # clear inputs
    document.getElementById('first_name').value = ""
    document.getElementById('last_name').value = ""


# show initial predefined members
initial_master = grade7 | grade8 | grade9 | grade10
initial_sorted = sorted(initial_master)
initial_total = len(initial_master)
initial_html = f"""
<div>
    <div><b>ALL MEMBERS ({initial_total}):</b></div>
    <div>{', '.join(initial_sorted)}</div>
    <div><b>TOTAL MEMBERS: {initial_total}</b></div>
</div>
"""
document.getElementById('output').innerHTML = initial_html
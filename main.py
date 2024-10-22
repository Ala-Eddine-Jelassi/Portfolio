import streamlit as st 

profile_page = st.Page(
    page="Pages/profile.py",
    title="My Profile ",
    icon= ":material/person:",
    default=True
)

V_card = st.Page(
    page="Pages/V_card.py",
    title="Create V-Card",
    icon=":material/cruelty_free:"
)
contact_page = st.Page(
    page="Pages/contact.py",
    title="Contact Me",
    icon=":material/alternate_email:"
)
projects_page = st.Page(
    page="Pages/projects.py",
    title="Projects ",
    icon=":material/emoji_objects:"
)
ideas_page= st.Page(
    page="Pages/ideas_page.py",
    title="Ideas ",
    icon=":material/neurology:"

)
#pg = st.navigation(pages=[profile_page,about_page,contact_page])
pg = st.navigation(
    {
        "Info" :[profile_page],
        "Contact":[contact_page],
        "Projects & Ideas":[projects_page,ideas_page]
    }
)
pg.run()

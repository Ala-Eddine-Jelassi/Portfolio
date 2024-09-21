import streamlit as st 

profile_page = st.Page(
    page="Pages/profile.py",
    title="Profile Page",
    icon= ":material/person:",
    default=True
)

about_page = st.Page(
    page="Pages/about.py",
    title="About Page",
    icon=":material/cruelty_free:"
)
contact_page = st.Page(
    page="Pages/contact.py",
    title="Contact Page",
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
        "Info" :[profile_page,about_page],
        "Contact":[contact_page],
        "Projects & Ideas":[projects_page,ideas_page]
    }
)
pg.run()

# License Management


# Modifying Models
    - In order to use manage commands like "makemigrations" and "migrate":
        you have to go into licensemgmt/settings.py and wrap the sqllite3 database base dir
        with the str() method. This prevents a POSIX Path error. Unfortunately, doing this
        breaks the /admin page. So once you're done migrating, remove the str() method.
        You will then be able to run the fully functioning app again.

    - This is obviously a pain in the neck and im certain there's a better way,
        but for now, that's what we're working with

    - If you do edit the models, be sure to update dashboard/admin.py to add/remove fields.
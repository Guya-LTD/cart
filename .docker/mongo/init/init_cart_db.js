db.createUser(
    {
        user : "cart_user",
        pwd  : "cart_password",
        roles : [
            {
                role : "readWrite",
                db   : "cart_db"
            }
        ]
    }
)
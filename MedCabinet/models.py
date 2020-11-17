from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()


class Strain(DB.Model):
    """
    Strains of the Mj
    """
    id = DB.column(DB.BigInteger,
                        primary_key=True)
    
    strain_name = DB.column(DB.String,
                            nullable=False)

    helps_with = DB.column(DB.String,
                                    nullable=False)

class Strain(DB.Model):
    """
    Strains of the Kush and their effects
    """
    id = DB.column(DB.In)
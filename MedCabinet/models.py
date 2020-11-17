from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()


class Strain(DB.Model):
    """
    Strains of the Mj
    """
    id = DB.column(DB.BigInteger)
    
    strain_name = DB.column(DB.String)

    helps_with = DB.column(DB.String,
                                    nullable=False)
    
    text = DB.column(DB.UnicodeText(2000))
    #TODO -- 
    
    # strain_id = DB.Column(DB.BigInteger,
    #                             DB.ForeignKey=('strain_name'))
from config import app, db, ma


class Genes(db.Model):
    __tablename__ = 'gene_autocomplete'
    id = db.Column('stable_id',db.String(80), primary_key=True)
    name = db.Column('display_label',db.String(80), unique=False)
    species = db.Column(db.String(120), unique=False)


class GeneSchema(ma.ModelSchema):
    class Meta:
        model = Genes
        sqla_session = db.session

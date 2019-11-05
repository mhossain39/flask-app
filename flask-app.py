#!flask/bin/python
from flask import request, jsonify, make_response
from flask import abort
from config import app, db, ma
from models import Genes, GeneSchema


@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('name', '')
    species = request.args.get('species', '')

    if (len(query) < 3) or species=="":
      abort(400)	
    names = Genes.query \
        .filter(Genes.name.like(query+'%')) \
        .filter(Genes.species == species) \
        .order_by(Genes.name).all()
 

    # Serialize the data for the response
    gene_schema = GeneSchema(many=True)
    return jsonify(gene_schema.dump(names).data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)



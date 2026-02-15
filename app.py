from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def izracunaj_godinu(godina):

    if godina <= 0:
        return "Godina ne može biti nula ili negativna."

    if godina > 3000:
        return "To je sada apsolutno nebitno. :)"

    poruka = ""
    if godina > 2200:
        poruka = "Otišli ste u daleku budućnost, ali ću Vam odgovoriti. ;)"

    mil = (godina - 1) // 1000 + 1
    vek = (godina - 1) // 100 + 1
    dec = (godina - 1) // 10 % 10 + 1

    mil_start = (mil - 1) * 1000 + 1
    mil_end = mil * 1000

    vek_start = (vek - 1) * 100 + 1
    vek_end = vek * 100

    dec_start = (dec - 1) * 10 + 1
    dec_end = dec * 10

    rezultat = f"""
{f"<b>{poruka}</b><br><br>" if poruka else ""}
<b>Godina {godina}:</b><br><br>
{mil}. milenijum<br>
{vek}. vek<br>
{dec}. decenija {vek}. veka<br><br>
<b>Objašnjenje:</b><br><br>
{mil}. milenijum: {mil_start}-{mil_end}<br>
{vek}. vek: {vek_start}-{vek_end}<br>
{dec}. decenija: {dec_start}-{dec_end}
"""

    return rezultat


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/izracunaj", methods=["POST"])
def izracunaj():

    data = request.json
    unos = data.get("godina", "").strip()

    if unos.endswith("."):
        unos = unos[:-1]

    try:
        godina = float(unos)
    except:
        return jsonify({"rezultat": "Greška! Morate uneti broj."})

    if not godina.is_integer():
        return jsonify({"rezultat": "Greška! Morate uneti ceo broj."})

    godina = int(godina)

    rezultat = izracunaj_godinu(godina)

    return jsonify({"rezultat": rezultat})


if __name__ == "__main__":
    app.run(debug=True)

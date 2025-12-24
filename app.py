# Flask kütüphanesini içe aktarıyoruz
from flask import Flask, render_template, request

# Modeli yüklemek için
import pickle
import pandas as pd

# Flask uygulamasını başlatıyoruz
app = Flask(__name__)

# Kaydedilmiş modeli yüklüyoruz
with open("final_model.pkl", "rb") as file:
    model = pickle.load(file)

# Ana sayfa
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    # Kullanıcı formu gönderirse
    if request.method == "POST":
        # Formdan gelen verileri alıyoruz
        year = int(request.form["year"])
        engine_size = float(request.form["engine_size"])
        mileage = float(request.form["mileage"])
        horsepower = float(request.form["horsepower"])
        brand = request.form["brand"]

        # Boş dataframe oluşturuyoruz
        data = {
            "const": 1,
            "year": year,
            "engine_size": engine_size,
            "mileage": mileage,
            "horsepower": horsepower,
            "brand_BMW": 0,
            "brand_Ford": 0,
            "brand_Honda": 0,
            "brand_Hyundai": 0,
            "brand_Mercedes": 0,
            "brand_Renault": 0,
            "brand_Volkswagen": 0
        }

        # Seçilen markayı 1 yapıyoruz
        data[f"brand_{brand}"] = 1

        # DataFrame'e çeviriyoruz
        df = pd.DataFrame([data])

        # Tahmin yapıyoruz
        prediction = int(model.predict(df)[0])

    return render_template("index.html", prediction=prediction)

# Flask uygulamasını çalıştırıyoruz
if __name__ == "__main__":
    app.run(debug=True)

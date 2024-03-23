import tkinter as tk
from tkinter import ttk
import requests
import apikey


class CryptoInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Info App")
        self.root.configure(bg="#1E1E1E")  # Fondo oscuro

        # Establecer dimensiones fijas
        window_width = 300
        window_height = 400
        self.root.geometry(f"{window_width}x{window_height}")

        # Evitar que la ventana sea redimensionada
        self.root.resizable(width=False, height=False)

        self.root.iconbitmap('C:\\Curso\\Python\\proyectos\\CryptoTracker\\Gartoon-Team-Gartoon-Action-Help-about'
                             '-star-fav.ico')

        self.label_crypto = ttk.Label(root, text="Ingrese la criptomoneda:", foreground="white", background="#1E1E1E")
        self.label_crypto.pack(pady=10)

        self.entry_crypto = ttk.Entry(root, style="TEntry")
        self.entry_crypto.pack(pady=10)

        self.button_search = ttk.Button(root, text="Buscar", command=self.get_crypto_info, style="TButton")
        self.button_search.pack(pady=10)

        self.label_result = ttk.Label(root, text="", foreground="white", background="#1E1E1E")
        self.label_result.pack(pady=10)

        #Estilos
        style = ttk.Style()
        style.configure("TButton", foreground="black", background="#333333", padding=(5, 5))
        style.configure("TEntry", fieldbackground="#333333", foreground="black")

    def get_crypto_info(self):
        crypto_symbol = self.entry_crypto.get().upper()  # Convertir a mayúsculas para consistencia
        api_url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        api_key = apikey.apikey  # Reemplaza con tu propia API key de CoinMarketCap

        params = {
            'start': '1',
            'limit': '100',
            'convert': 'USD'
        }

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': apikey.apikey,
        }

        try:
            response = requests.get(api_url, params=params, headers=headers)
            data = response.json()

            # Inicializar la cadena de resultados
            result_text = ""

            # Verificar si se proporciona una criptomoneda específica
            if crypto_symbol:
                for crypto in data['data']:
                    if crypto['symbol'] == crypto_symbol:
                        name = crypto['name']
                        price = crypto['quote']['USD']['price']
                        percent_change_1h = crypto['quote']['USD']['percent_change_1h']
                        percent_change_24h = crypto['quote']['USD']['percent_change_24h']

                        result_text = f"Información de {name} ({crypto_symbol}):\n\n"
                        result_text += f"Precio: ${price}\n"
                        result_text += f"Cambio en la última hora: {percent_change_1h}%\n"
                        result_text += f"Cambio en las últimas 24 horas: {percent_change_24h}%"
                        break  # Salir del bucle cuando se encuentra la criptomoneda

                if not result_text:
                    result_text = f"No se encontró información para {crypto_symbol}"

            else:
                # Si no se proporciona una criptomoneda específica, mostrar las 5 mejores
                for crypto in data['data'][:4]:
                    name = crypto['name']
                    price = crypto['quote']['USD']['price']
                    percent_change_1h = crypto['quote']['USD']['percent_change_1h']
                    percent_change_24h = crypto['quote']['USD']['percent_change_24h']
                    result_text += f"{name}:[ Precio: ${price}\n"
                    result_text += f"Cambio en la última hora: {percent_change_1h}%\n"
                    result_text += f"Cambio en las últimas 24 horas: {percent_change_24h}%]\n\n"


            self.label_result.config(text=result_text)

        except Exception as e:
            print(f"Error al obtener información: {e}")
            self.label_result.config(text="Error al obtener información")



if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoInfoApp(root)
    root.mainloop()


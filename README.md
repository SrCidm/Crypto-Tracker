
This project is a desktop application developed in Python using the Tkinter library for the graphical user interface. The application, called "Crypto Info App," allows users to retrieve information about cryptocurrencies using the CoinMarketCap API.

The application consists of a main window with an input field for users to enter the symbol of the cryptocurrency they want to look up, a button to perform the search, and a label where the retrieved information is displayed.

When the user enters the symbol of a cryptocurrency and presses the search button, the application makes a request to the CoinMarketCap API to fetch the most recent information about that cryptocurrency. The retrieved information includes the cryptocurrency's name, its current price in US dollars (USD), and the changes in price over the last hour and the last 24 hours.

If a specific cryptocurrency symbol is not provided, the application will display information about the top five cryptocurrencies in terms of market capitalization.

The project uses custom styles for the user interface elements and is configured to prevent the window from being resized. Additionally, error handling is implemented to notify the user if there is any issue retrieving information from the API.

In summary, this application provides a simple and convenient way for users to obtain up-to-date information about cryptocurrencies quickly and easily through an intuitive graphical interface.

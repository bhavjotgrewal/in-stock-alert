# in-stock-alert
A tool to determine if products are in stock.

# Why? #

During the current unprecedented situation, finding stock for GPUs, some CPUs, and consoles has been incredibly difficult. I wanted to help people find products they want and let them have a chance against bots and scalpers. Many people do not have the time to be at their computers all day, and this tool helps automate the process of finding stock. While there are stock livestreams available, this tool should be faster as it is run locally. 

# How does it work? #

Scraping sites is challenging due to anti-bot protection. However, it can be done using proxies. This ensures that you do not send too many requests from a single address, and thus are not blocked. This tool uses proxies that the user provides in order to run it' scripts. Beautiful soup is used along with multithreading to increase the scrape speed. Results are displayed using Rich in a seperate window. 

# How do I run it? #

Simply run the .exe in /bin! 


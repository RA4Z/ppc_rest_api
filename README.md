## PPC API - WEG Energy

This repository contains the source code for the PPC (Production Planning and Control) department's REST API at WEG Energy. The API serves as a central hub for connecting various artificial intelligence services and databases, facilitating access to and utilization of relevant information for the department.

### Features

The PPC API offers the following functionalities:

* **Connection with Artificial Intelligence:**
    * **Document Search:** Enables intelligent search within internal documents, leveraging natural language processing to find relevant information quickly and efficiently.
    * **Secretary Assistant:** Automates administrative tasks such as scheduling meetings, organizing emails, and managing contacts.
    * **PPC Chatbot:** Conversational interface for quick access to information and performing PPC-related tasks, such as checking production status and updating schedules.
* **Database Queries:**
    * The API performs structured queries on relevant department databases, returning information formatted in JSON for easy consumption by other applications and dashboards.

### Technologies Used

* **Programming Language:** Python
* **Web Framework:** Flask
* **Data Format:** JSON

### Installation and Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RA4Z/ppc_rest_api.git
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   * Create a `.env` file in the project root with the necessary settings, such as database credentials and external API keys.
5. **Start the server:**
   ```bash
   flask run
   ```
   The API will be available at `http://127.0.0.1:5000/`.

### Contact

If you have any questions or problems, please contact Robert Aron Zimmermann at robert@weg.net.

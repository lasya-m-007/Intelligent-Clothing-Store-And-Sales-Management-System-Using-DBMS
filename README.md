👕 IntelliWear – Smart Clothing Store Management System
  IntelliWear is a full-stack web application designed to help clothing store owners manage their business efficiently. It provides features for inventory management, sales tracking, billing, and analytics — all in one place.
  🚀 Features
    🔐 Authentication
      Secure login system using sessions
      Restricted access to authorized users only
    📊 Dashboard
      View key business metrics:
      Total Products
      Total Sales
      Total Revenue
      Low Stock Items
      Quick navigation for core actions
    📦 Product Management
      Add new products
      Edit existing products
      Delete products
      Track stock levels
      Highlight low-stock items
    💳 Sales Management
      Search products by ID
      Generate bills based on quantity
      Automatic stock updates after sales
      Maintain complete sales history
  🛠️ Tech Stack
    Frontend:
      HTML5
      CSS3 (Modern responsive UI)
    Backend:
      Python (Flask)
    Database:
      MySQL
  📁 Project Structure
  IntelliWear/
  │
  ├── app.py                # Main Flask application
  ├── static/
  │   └── style.css        # Styling
  │
  ├── templates/
  │   ├── index.html       # Login & Landing page
  │   ├── dashboard.html   # Dashboard view
  │   ├── products.html    # Product management
  │   └── sales.html       # Sales system
  │
  └── database (MySQL)

⚙️ Installation & Setup
    1. Clone the Repository
      git clone https://github.com/your-username/intelliwear.git
      cd intelliwear
    2. Create Virtual Environment
      python -m venv venv
      source venv/bin/activate   # Mac/Linux
      venv\Scripts\activate      # Windows
    3. Install Dependencies
      pip install flask mysql-connector-python
    4. Setup MySQL Database
        Create a database:
        CREATE DATABASE dbms_clothing;
        Create required tables:
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50),
            password VARCHAR(50)
        );
        CREATE TABLE products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            category VARCHAR(100),
            price FLOAT,
            stock INT
        );
        CREATE TABLE sales (
            sale_id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            product_name VARCHAR(100),
            qty INT,
            total FLOAT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
      5. Update Database Credentials
        In app.py, update:
          db = mysql.connector.connect(
              host="localhost",
              user="root",
              password="your_password",
              database="dbms_clothing"
          )
      6. Run the Application
        python app.py
        Open in browser:
        http://127.0.0.1:5001
🎯 How It Works
  User logs in
    Dashboard displays business insights
    Products can be added/edited/deleted
    Sales are recorded with automatic billing
    Inventory updates automatically after each sale
  📱 UI Highlights
    Modern dashboard design
    Sidebar navigation with hover animation
    Responsive layout for mobile devices
    Clean tables and forms
    Visual indicators for stock levels
  🔮 Future Enhancements
    Barcode scanning for products
    Customer management system
    Invoice PDF generation
    AI-based sales insights
    Online cloud deployment
  👩‍💻 Author
    Lasya Mandapati
    G. Mary Shainy
  DBMS Project – 2026
  📌 License
  This project is for educational purposes.







Video (24951A6686) : https://youtu.be/CX_ZkvDR-s4
Video (24951A6699) : 

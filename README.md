# Google Maps Pipeline Project

## Project Overview

The goal of this task is to clean, import, analyze, and visualize location-based data related to restaurants and places in Dudweiler and the Saarland Informatics Campus (SIC) in Saarbrücken. This project utilizes SQL for data storage, Google APIs for geolocation, and presents insights using SQL queries and geospatial visualizations.

The project is broken down into several tasks:

- **Data Cleaning & Importing**: Extract and clean the given dataset, and import relevant columns into a relational database.
- **Filtering & Statistics**: Filter places in Dudweiler and provide statistics (total number of places, types of restaurants, etc.).
- **Finding the 5 Nearest Restaurants**: Use Google API to reverse geocode the location of Saarland Informatics Campus and find the closest restaurants.
- **Identifying the Best Restaurant**: Choose the best restaurant based on criteria like Google ratings and distance from SIC.
- **Distance Calculation & Route Suggestions**: Calculate distances between the chosen restaurant and SIC, and suggest car/public transit routes.
- **Code Readability & Documentation**: Ensure the code is well-documented with markdown and inline comments.
- **Bonus Task**: Integrate additional APIs, provide insights, and create geospatial visualizations (e.g., clustering, heatmaps).

### Technologies Used

- **Python**: For data processing, SQL querying, API integration, and visualization.
- **Flask**: Web framework used to create the dashboard.
- **Google APIs**: For geolocation services like reverse geocoding and route suggestions.
- **SQL**: Relational database management system (SQLite) for data storage.
- **HTML/CSS**: For the web interface of the dashboard.
- **JavaScript (Leaflet)**: For displaying interactive maps and geospatial visualizations.

### File Structure

- `static/maps/`: Contains HTML files for different maps (cluster map, distance map, etc.).
- `templates/`: Contains HTML templates for the Flask application.
- `app.py`: Main Python file to run the Flask app and handle routing.
- `requirements.txt`: Contains all the required dependencies for the project.
- `data/`: Contains the dataset and supporting files.
  - `Dudweiler-data.xlsx`: The raw data for the project, containing information about places in Dudweiler.
  - `db object`: The database object used to interact with the SQL database.
  - `data.ipynb`: Jupyter notebook containing the data cleaning, analysis, and visualization code.
  - `cluster_map.html`, `distance_clusters_map.html`, `heatmap.html`, `restaurants_distances_map.html`, `routes_map.html`: HTML files for the geospatial visualizations.

### Setup Instructions

1. **Clone the Repository**:
    - Clone the project to your local machine:
      ```bash
      git clone <repository-url>
      ```

2. **Set Up the Virtual Environment**:
    - Create a virtual environment:
      ```bash
      python3 -m venv venv
      ```
    - Activate the virtual environment:
      - On Windows:
        ```bash
        venv\Scripts\activate
        ```
      - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Install Dependencies**:
    - Install the required packages from `requirements.txt`:
      ```bash
      pip install -r requirements.txt
      ```

4. **Run the Flask App**:
    - Run the Flask application:
      ```bash
      python app.py
      ```
    - Open your browser and go to `http://127.0.0.1:5000/` to see the dashboard in action.

### `requirements.txt`

This project requires the following Python packages:

```txt
Flask==2.2.2
pymysql==1.0.2       # MySQL client library (use this for MySQL)
psycopg2==2.9.3      # PostgreSQL client library (use this for Postgres)
googlemaps==4.0.1    # Google Maps API client library
geopy==2.3.0         # Geocoding library for additional geolocation handling
Flask-SQLAlchemy==2.5.1 # SQLAlchemy ORM for database interaction
```

You can install the dependencies by running:

```bash
pip install -r requirements.txt
```

### Task Breakdown

1. **Data Cleaning & Importing**: 
    - Extracted relevant columns from `Dudweiler-data.xlsx` and imported them into a relational database.
    - Chose SQLite for database management due to the need for fast querying and scalability.

2. **Filtering & Statistics**: 
    - Filtered places based on zip code `66125` for Dudweiler and provided statistics (total places, number of restaurants, different types of restaurants, etc.).

3. **Finding the 5 Nearest Restaurants**:
    - Used the Google Maps API to reverse geocode the location "Saarland Informatics Campus 66123 Saarbrücken" and found the 5 closest restaurants from the database.

4. **Identifying the Best Restaurant**:
    - Selected the best restaurant based on Google ratings and distance from SIC.
    - Included details like name, phone number, contact info, and opening hours.

5. **Distance Calculation & Route Suggestions**:
    - Calculated the distance between SIC and the selected restaurant.
    - Used the Google Maps API to suggest driving and public transit routes.

6. **Geospatial Visualizations**:
    - Created interactive maps (cluster map, distance map, heatmap, etc.) and integrated them into the Flask dashboard using HTML iframes.

### Bonus Task

- **Geospatial Visualizations**: 
    - Added geospatial visualizations like clustering and heatmaps for restaurant locations.

### Conclusion

This project demonstrates how to leverage SQL, Google Maps APIs, and geospatial visualizations to analyze and present location-based data. By providing an interactive web dashboard, the project showcases insights such as the closest restaurants to SIC, the best restaurant, and potential routes.

### Future Work

- **Automating Google API Queries**: To handle a large number of API requests in the future, the system can be scaled to automatically query the Google API in bulk.
- **Expanding the Data**: Integrating more datasets related to restaurants and other places in Saarbrücken or beyond.
- **Enhancing Visualizations**: Adding more advanced visualizations or interactive features to the dashboard.


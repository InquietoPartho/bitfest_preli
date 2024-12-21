# bitfest_preli

# Challenge 02: Mofa's Kitchen Buddy API

This is the backend API for **Mofa's Kitchen Buddy**, a kitchen management system designed to help users manage ingredients, store and retrieve recipes, and interact with a chatbot for recipe suggestions. The API allows users to add, update, and retrieve ingredients and recipes, and interact with a chatbot to suggest recipes based on preferences like cravings for sweet or savory dishes.

## Features

1. **Ingredient Management**:

   - Add new ingredients to your kitchen.
   - Update ingredient quantities.
   - Retrieve a list of all available ingredients.

2. **Recipe Management**:

   - Input favorite recipes (both text and image-based).
   - Retrieve recipes based on available ingredients.

3. **Chatbot Interaction**:
   - Communicate with the chatbot to get recipe suggestions based on your preferences (e.g., "I want something sweet").

## API Endpoints

### 1. Ingredient Management

#### **Add a new ingredient**

- **Endpoint**: `POST /api/ingredients`
- **Description**: Add a new ingredient to the database.
- **Request Body**:
  ```json
  {
    "name": "Tomato",
    "quantity": "2"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Ingredient added successfully!"
  }
  ```

#### **Update an ingredient**

- **Endpoint**: `PUT /api/ingredients/{id}`
- **Description**: Update an ingredient’s name or quantity.
- **Request Body**:
  ```json
  {
    "name": "Sugar",
    "quantity": "1kg"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Ingredient updated successfully!"
  }
  ```

#### **Get all ingredients**

- **Endpoint**: `GET /api/ingredients`
- **Description**: Retrieve a list of all ingredients.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Sugar",
      "quantity": "500g"
    },
    {
      "id": 2,
      "name": "Tomato",
      "quantity": "2"
    }
  ]
  ```

### 2. Chatbot Interaction

#### **Chat with the chatbot**

- **Endpoint**: `POST /api/chat`
- **Description**: Communicate with the chatbot to get recipe suggestions based on your preferences.
- **Request Body**:
  ```json
  {
    "message": "I want something sweet today"
  }
  ```
- **Response**:
  ```json
  {
    "response": "That sounds lovely! To give you the best sweet treat recommendation, I need a little more information.  What kind of sweet are you craving?  For example:\n\n* **Do you want something baked or something more like candy?**\n* **Do you prefer chocolate, fruit, caramel, vanilla, etc.?**\n* **How much time do you have to prepare it?** (e.g., something quick and easy, or something more involved?)\n* **Do you have any dietary restrictions or preferences?** (e.g., vegan, gluten-free, low-sugar)\n\nOnce I know a bit more, I can give you a more specific suggestion!\n"
  }
  ```

---

## Running the Application

### Prerequisites

1. **Python 3.9+** installed.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. Run the script to create the SQLite database and tables:
   ```bash
   python models/ingredients.py
   ```

### Running the Flask App

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. The app will run on `http://127.0.0.1:5000/`.

### Testing with Postman

You can use **Postman** to test the API by sending requests to the corresponding endpoints.

1. **Test Ingredient Management**:

   - Add a new ingredient by sending a `POST` request to `http://127.0.0.1:5000/api/ingredients` with a JSON body.
   - Update an ingredient with a `PUT` request to `http://127.0.0.1:5000/api/ingredients/{id}`.
   - Retrieve all ingredients using a `GET` request to `http://127.0.0.1:5000/api/ingredients`.

2. **Test Chatbot**:
   - Send a `POST` request to `http://127.0.0.1:5000/api/chat` with a JSON body like `{"message": "I want something sweet today"}`.

const add_button = document.getElementById('add-button');
const inputField = document.getElementById('input-field');
const ulEl = document.getElementById('shopping-list');

// Fetch items from local storage when the page loads
window.addEventListener('load', function () {
  const itemsFromLocalStorage = JSON.parse(localStorage.getItem('shoppingList')) || [];
  itemsFromLocalStorage.forEach(item => appendListItems(item));
});

add_button.addEventListener("click", addItem);

inputField.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    addItem();
  }
});

function addItem() {
  let inputValue = inputField.value.trim();
  if (inputValue !== "") {
    appendListItems(inputValue);

    // Save items to local storage
    saveToLocalStorage(inputValue);

    // Clear input field and focus on it
    clearInputFieldEl();
    inputField.focus();
  }
}

function clearShoppingListEl() {
  ulEl.innerHTML = "";
}

function clearInputFieldEl() {
  inputField.value = "";
}

function appendListItems(item) {
  let newEl = document.createElement("li");
  newEl.textContent = item;

  newEl.addEventListener("click", function () {
    newEl.remove();
    // Remove item from local storage when it's removed from the list
    removeFromLocalStorage(item);
  });

  ulEl.append(newEl);
}

function saveToLocalStorage(item) {
  const itemsFromLocalStorage = JSON.parse(localStorage.getItem('shoppingList')) || [];
  itemsFromLocalStorage.push(item);
  localStorage.setItem('shoppingList', JSON.stringify(itemsFromLocalStorage));
}

function removeFromLocalStorage(item) {
  const itemsFromLocalStorage = JSON.parse(localStorage.getItem('shoppingList')) || [];
  const updatedItems = itemsFromLocalStorage.filter(i => i !== item);
  localStorage.setItem('shoppingList', JSON.stringify(updatedItems));
}


// sending data to backend to falsk app.py
function sendDataToBackend() {
  const items = JSON.parse(localStorage.getItem('shoppingList')) || [];
  fetch('/submit_items', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ items: items })
  })
    .then(response => response.text())
    .then(data => {
      console.log(data); // Print response from backend in console
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

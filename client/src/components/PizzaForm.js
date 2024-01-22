import { useEffect, useState } from "react";
import { useHistory } from "react-router";
// import { useHistory } from "react-router-dom/cjs/react-router-dom.min";

function PizzaForm() {
  const [pizzas, setPizzas] = useState([]);
  const [restaurants, setRestaurants] = useState([]);
  const [pizzaId, setPizzaId] = useState("");
  const [restaurantId, setRestaurantId] = useState("");
  const [price, setPrice] = useState("");
  const [formErrors, setFormErrors] = useState([]);

  const history = useHistory()

  useEffect(() => {
    fetch("/pizzas")
      .then((r) => r.json())
      .then(setPizzas);
  }, []);

  useEffect(() => {
    fetch("/restaurants")
      .then((r) => r.json())
      .then(setRestaurants);
  }, []);


  function handleSubmit(e) {
    e.preventDefault();
    const formData = {
      pizza_id: pizzaId,
      restaurant_id: restaurantId,
      price: parseInt(price),
    };
    fetch("/restaurant_pizzas", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    }).then((r) => {
      if (r.ok) {
        history.push(`/restaurants/${restaurantId}`);
        // r.json().then((newRestaurantPizza) => {
        //   // onAddPizza(newPizza);
        //   setFormErrors([]);
        // });
      } else {
        r.json().then((err) => setFormErrors(err.errors));
      }
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="pizza_id">Pizza:</label>
      <select
        id="pizza_id"
        name="pizza_id"
        value={pizzaId}
        onChange={(e) => setPizzaId(e.target.value)}
      >
        <option value="">Select a pizza</option>
        {pizzas.map((pizza) => (
          <option key={pizza.id} value={pizza.id}>
            {pizza.name}
          </option>
        ))}
      </select>
      <label htmlFor="restaurant_id">Restaurant:</label>
      <select
        id="restaurant_id"
        name="restaurant_id"
        value={restaurantId}
        onChange={(e) => setRestaurantId(e.target.value)}
      >
        <option value="">Select a restaurant</option>
        {restaurants.map((restaurant) => (
          <option key={restaurant.id} value={restaurant.id}>
            {restaurant.name}
          </option>
        ))}
      </select>


      <label htmlFor="price">Price:</label>
      <input
        type="number"
        name="price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />
      {formErrors.length > 0
        ? formErrors.map((err) => (
            <p key={err} style={{ color: "red" }}>
              {err}
            </p>
          ))
        : null}
      <button type="submit">Add To Restaurant Pizza</button>
    </form>
  );
}

export default PizzaForm;

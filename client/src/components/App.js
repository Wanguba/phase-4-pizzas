import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import axios from 'axios';
import Home from "./Home";
import Restaurant from "./Restaurant"

const Restaurants = () => {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    axios.get('/restaurants')
      .then(response => setRestaurants(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Restaurants</h1>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.id}>
            <Link to={`/restaurants/${restaurant.id}`}>
              <h2>{restaurant.name}</h2>
            </Link>
            <p>{restaurant.address}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

// const RestaurantDetails = ({ match }) => {
//   const [restaurant, setRestaurant] = useState(null);

//   useEffect(() => {
//     const restaurantId = match.params.id;
//     axios.get(`http://localhost:5000/restaurants/${restaurantId}`)
//       .then(response => setRestaurant(response.data))
//       .catch(error => console.error(error));
//   }, [match.params.id]);

//   if (!restaurant) {
//     return <p>Loading...</p>;
//   }

//   return (
//     <div>
//       <h1>{restaurant.name}</h1>
//       <p>{restaurant.address}</p>
//       <h2>Pizzas</h2>
//       <ul>
//         {restaurant.pizzas.map(pizza => (
//           <li key={pizza.id}>
//             <h3>{pizza.name}</h3>
//             <p>{pizza.ingredients}</p>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/restaurants/:id" component={Restaurant} />
        <Route path="/restaurants" component={Restaurants} />
        <Route path="/pizzas" />
        <Route path="/" component={Home} />
      </Switch>
    </Router>
  );
};

export default App;


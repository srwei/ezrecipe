import React, { Component } from "react";
//import axios from "axios";
import IngredientForms from "./components/IngredientForms";
//import IngredientList from "./components/IngredientList";

class App extends Component {

  render() {
    return (
      <div className="App">
        <IngredientForms />
        {/* <IngredientList /> */}
      </div>
    );
  }
}


    

export default App;
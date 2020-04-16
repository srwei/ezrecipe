import React, { Component } from "react";
import { BrowserRouter, Route, Redirect, Switch } from 'react-router-dom'
//import axios from "axios";
import IngredientForms from "./components/IngredientForms";
import IngredientList from "./components/IngredientList";

class App extends Component {

  render() {
    return (
      <BrowserRouter>
        <Switch>
            <Route exact path='/ezrecipe' component={IngredientForms}/>
            <Route exact path='/ezrecipe/ingredient_list' component={IngredientList}/>
        </Switch>
      </BrowserRouter>
    );
  }
}


    

export default App;
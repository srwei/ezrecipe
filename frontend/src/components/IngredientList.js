import React, { Component } from 'react'
import axios from "axios"

class IngredientList extends React.Component {
    constructor(props) {
      super(props)
  
      this.state = {
        ingredients: [],
        recipes: []
      }
    }
  
    componentDidMount() {
      axios.get('http://localhost:8000/api/ingredients')
        .then(response => {
          console.log(response)
          this.setState({ingredients: response.data})
        })
        .catch(error => {
          console.log(error)
        })
    }
    
    render () {
      const { ingredients } = this.state
      return (
        <div>
          List of ingredients
          {
            ingredients.length ?
            ingredients.map(ingredients => <div key={ingredients.ngredient_id}>{ingredients.ingredient_name}</div>) :
            null
          }
        </div>
      )
    }
  }

export default IngredientList
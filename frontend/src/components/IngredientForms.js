import React, { Component } from 'react'
import axios from 'axios'

class IngredientForms extends Component {
    constructor(props) {
        super(props)

        this.state = {
            ingredients_str: [{ ingredient: "" }]
        }
    }

    changeIngredientHandler = idx => e => {
        const newIngredients = this.state.ingredients_str.map((ingredient, sidx) => {
            if (idx !== sidx) {return ingredient};
            return { ingredient: e.target.value };
            });
            this.setState({ ingredients_str: newIngredients });
    }

    changeHandler = (e) => {
        this.setState(
            { ingredients_str: e.target.value }
        )
    }

    addIngredientHandler = () => {
        this.setState({
            ingredients_str: this.state.ingredients_str.concat([{ ingredient: "" }])
        })
    }

    removeIngredientHandler = idx => () => {
        this.setState({
            ingredients_str: this.state.ingredients_str.filter((s, sidx) => idx !== sidx)
        })
    }

    submitHandler = e => {
        e.preventDefault()

        //console.log(this.state)
        let res = this.state.ingredients_str
        res = res.map(a => a.ingredient)
        //console.log(res)
        
        var post = { ingredients_str: res }
        console.log(post)
        axios.post('http://localhost:8000/api/inputingredients/', post)
            .then(response => {
                console.log(response)
                console.log(response.data)
            })
    }

    render() {
        return (
            <div>
                <form onSubmit={this.submitHandler}>
                    <div>
                        <h4>Ingredients</h4>

                        {this.state.ingredients_str.map((ingredient, idx) => (
                            <div className="ingredient">
                                <input  
                                    type="text" 
                                    placeholder={ `Ingredient #${idx + 1} name`} 
                                    value={ingredient.ingredient}
                                    onChange={this.changeIngredientHandler(idx)}
                                />
                                <button
                                    type="button"
                                    onClick={this.removeIngredientHandler(idx)}
                                    className="small"
                                >
                                  -
                                </button>
                            </div>
                        ))}
                        <button
                            type="button"
                            onClick={this.addIngredientHandler}
                            className="small"
                        >
                            Add Ingredient
                        </button>
                    </div>
                    <button 
                    type="submit">Submit
                    </button>
                </form>
            </div>
        )
    }
}

export default IngredientForms

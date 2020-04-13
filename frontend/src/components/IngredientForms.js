import React, { Component } from 'react'
import axios from 'axios'

class IngredientForms extends Component {
    constructor(props) {
        super(props)

        this.state = {
            ingredient_name: ''
        }
    }

    changeHandler = (e) => {
        this.setState(
            { ingredient_name: e.target.value }
        )
    }

    submitHandler = e => {
        e.preventDefault()
        console.log(this.state)
        axios.post('http://localhost:8000/api/inputingredients/', this.state)
            .then(response => {
                console.log(response)
            })
    }

    render() {
        const { ingredient_name } = this.state
        return (
            <div>
                <form onSubmit={this.submitHandler}>
                    <div>
                        <input 
                            type="text" 
                            name="ingredient_name" 
                            value={ingredient_name} 
                            onChange={this.changeHandler} 
                        />
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </div>
        )
    }
}

export default IngredientForms

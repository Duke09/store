import React, {Component} from 'react';

class PizzaDetail extends Component{
    render(){
        const obj = this.props.pizzeriaDetail;
        return(
            <div style={{color:"yellow", border:"1px solid yellow"}}>
                <h4>{obj.pizzeria_name}</h4>
                <h6>{obj.street}, {obj.city}, {obj.state} - {obj.zip_code}</h6>
                <h6>{obj.phone_number}</h6>
                <p>{obj.description}</p>
            </div>
        )
    }
}

export default PizzaDetail;
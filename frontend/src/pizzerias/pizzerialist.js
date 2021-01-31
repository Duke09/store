import React, {Component} from 'react';
import axios from 'axios';
import PizzaDetail from './pizzeriadetail';

class PizzaList extends Component{
    constructor(props){
        super(props);
        this.state = {
            pizzeriaData: [],
            pizzeria: " ",
            showComponent: false,
        };
        this.getPizzaDetail=this.getPizzaDetail.bind(this);
        this.showPizzeriaDetails=this.showPizzeriaDetails.bind(this);
    }

    getPizzaDetail(item){
        axios
        .get("http://127.0.0.1:8000".concat(item.absolute_url))
        .then((response) => {
            this.setState({pizzeria: response.data})
        })
        .catch(function(error){
            console.log(error);
        });
    }

    showPizzeriaDetails(item){
        this.getPizzaDetail(item);
        this.setState({showComponent: true});
    }

    componentDidMount(){
        axios
        .get("http://127.0.0.1:8000/")
        .then((response) => {
            console.log(response)
            this.setState({
                pizzeriaData: response.data
            })
        })
    }

    render(){
        return(
            <div>
                {
                    this.state.pizzeriaData.map((item) => {
                        return (
                            <h6 key={item.id} onClick={() => this.showPizzeriaDetails(item)}>{item.pizzeria_name}, {item.city}</h6>
                        );
                    })
                }
                {
                    this.state.showComponent ? (
                        <PizzaDetail pizzeriaDetail={this.state.pizzeria}/>
                    ) : null
                }
            </div>
        );
    }
}

export default PizzaList;
import React from 'react';
import ReactDOM from 'react-dom';
import '../css/auth.css';
import '../css/basic.css';

export class FirstPage extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.state = {};
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmit(event) {
        alert(this.state);
        event.preventDefault();
    }

    Main = () => {
        return <main className={'main'}>
            {this.Inner_container()}</main>;
    }
    ContainerTitle = () => {
        return <h1 className={'container_title'}>GoToCredit</h1>;
    }

    ContainerText = () => {
        return <h2 className={'container_text'}>Всего 3 шага до вашей мечты!</h2>;
    }

    Footer = () => {
        return <footer className={'footer'}>{this.Footer_text()}</footer>;
    }

    Footer_text = () => {
        return <h3 className={'footer_text'}>По всем вопросам писать сюда - @tvorogme</h3>;
    }

    AuthButton = () => {
        return <a className={'AuthButton'} value={'auth'}
                  href={"https://stonks.goto.msk.ru/o/authorize/?state=random_state_string&client_id=M2mY5d4b6NcVKxr2XqKXSxZgpk78WK6ZaU3IxYDd&response_type=code"}>
            Auth!
        </a>;
    }

    Inner_container = () => {
        return <div className={'inner_container'}>
            {this.ContainerTitle()}
            {this.ContainerText()}
            {this.AuthButton()}
        </div>;
    }

    render() {
        return (
            <div>
                {this.Main()}
                {this.Footer()}
            </div>
        );
    }
}


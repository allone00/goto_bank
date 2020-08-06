import React from 'react';
import '../css/basic.css';
import '../css/main.css';

function Submit() {
    let formData = {};

    let requestUrl = 'https://bank.goto.msk.ru/form/';
    let url = window.location.search;

    let token = url.slice(6, url.length);

    // console.log(url);

    const send_message = (formData) => { fetch('/api/qwerty', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData

    })
        .then(response => console.log('message send with fetch!'))
        .catch(error => console.log(error))
    };

    formData['mac'] = document.querySelector('.MacInput').value;
    formData['sum'] = document.querySelector('.AmountInput').value;
    formData['code'] = token;

    send_message(JSON.stringify(formData));

    document.querySelector('.MacInput').value = '';
    document.querySelector('.AmountInput').value = '';

    alert('Мы рассмотрим заявку в течении 72 часов!\n С любовью GoToBank!');
}


export class MainPage extends React.Component {
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

    RequestButton = () => {
        return <a className={'RequestButton'} value={'register'} onClick={Submit}>
            Click!
        </a>;
    }

    Inner_container = () => {
        return <div className={'inner_container'}>
            {this.ContainerTitle()}
            {this.ContainerText()}
            {this.Form()}
        </div>;
    }

    Form = () => {
        return (<form className={'form'} method={'post'} onSubmit={this.handleSubmit}>
            <label htmlFor={'Mac_field'} className={'MacForm'}>Mac-address: <br/>
                <input type={'text'} id={'Mac_field'} name={'macField'} className={'MacInput'} pattern={'[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}'} placeholder={'AA-AA-AA-AA-AA-AA'} onChange={this.handleChange}/>
            </label>
            <label htmlFor={'Amount_field'} className={'AmountForm'}>Сумма:<br/>
                <input type={'number'} min={'1'} max={'10000'} id={'Amount_field'} name={'amountField'} className={'AmountInput'} placeholder={'99999999'} onChange={this.handleChange}/>
            </label>
            <div className={'ButtonBox'}>
                {this.RequestButton()}
            </div>
        </form>)
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


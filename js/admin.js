import React from 'react';
import '../css/admin.css';
import '../css/basic.css';

function get_json() {

    let get_message = fetch('/api/credit')
        .then((response) => {
                if (response.status !== 200) {
                    console.log(error);
                    return;
                }
                response.json().then((data) => {
                    return data;
                });
            }
        )
        .catch(error => console.log(error));

    return get_message;
}

function send_data() {

    let parent = document.querySelector('.list');

    let data = {};

    let list_elements = document.querySelectorAll('.list-elem');

    let sections = document.querySelectorAll('.select');

    for (let i = 0; i < list_elements.length; ++i) {
        data[`${list_elements[i].dataset.id}`] = sections[i].value == 'true' ? true : false;
    }

    // console.log(data, list_elements, sections);

    if (parent.hasChildNodes()) {
        for (let elem in document.querySelectorAll('.list-elem')) {
            parent.remove(elem);
        }
    }
    else {
        alert('Заявок не обнаружено!');
    }


    const send_message = (data) => { fetch('/api/credit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: data

    })
        .then(response => console.log('message send with fetch!'))
        .catch(error => console.log(error))
    };

    send_message(data);

}

export class AdminPage extends React.Component {
    Header = () => {
        return <header className={'header'}>
            <nav className={'nav'}>
                <h2 className={'nav-elem'}>Имя</h2>
                <h2 className={'nav-elem'}>Сумма</h2>
                <h2 className={'nav-elem'}>Проценты</h2>
                <h2 className={'nav-elem'}>Статус</h2>
            </nav>
        </header>;
    }

    Main = () => {
        return <main className={'Main'}>
            {this.List()}
            {this.Button()}
        </main>;
    }

    List = () => {
        let data = get_json();
        const listItems = data.map((item) =>
            <li className={'list-elem'} data-id={`${item.id}`}><span>{item.full_name}</span> <input className={'input'} type={'number'} defaultValue={item.sum}/> <input className={'input'} type={'number'} defaultValue={item.interest * 100}/>
                <select className={'select'}>
                    <option value={'true'}>Одобрено</option>
                    <option value={'false'}>Не одобрено</option>
                </select>
            </li>
        );

        // console.log(this.props);

        return <ul className={'list'}>{listItems}</ul>;
    }

    Button = () => {
        return <a className={'button'} href={'#'} onClick={send_data}>Click!</a>;
    }

    render() {
        return <div>
            {this.Header()}
            {this.Main()}
        </div>;
    }
}

import React from 'react';
import '../css/admin.css';
import '../css/basic.css';

function get_json() {

    let get_message = fetch('./api/application.json')
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
        let data = [{'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000}];

        const listItems = data.map((item) =>
            <li className={'list-elem'}><span>{item.name}</span> <input className={'input'} type={'number'} value={item.sum}/> <input className={'input'} type={'number'} value={item.percents * 100}/>
                <select className={'select'}>
                    <option value={'true'}>Одобрено</option>
                    <option value={'false'}>Не одобрено</option>
                </select>
            </li>
        );

        return <ul className={'list'}>{listItems}</ul>;
    }

    Button = () => {
        return <a className={'button'} href={'#'}>Click!</a>;
    }

    render() {
        return <div>
            {this.Header()}
            {this.Main()}
        </div>;
    }
}

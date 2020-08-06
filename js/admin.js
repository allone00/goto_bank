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
            <h2 className={'header-title'}>Заявки</h2>
        </header>;
    }

    Main = () => {
        return <main className={'Main'}>{this.List()}</main>;
    }

    List = () => {
        let data = [{'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000},
            {'token': '123', 'name': 'Иван Петрович', 'user_email': 'example@example.com', 'mac': 'aa-aa-aa', 'percents': 0.36, 'sum': 12000}];

        const listItems = data.map((item) =>
            <li>{item.name} {item.sum} {item.percents}</li>
        );

        return <ul>{listItems}</ul>;
    }


    render() {
        return <div>
            {this.Header()}
            {this.Main()}
        </div>;
    }
}
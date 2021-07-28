import React from 'react';
import logo from './logo.svg';
import './App.css';
import APIUserList from './components/APIUser.js';
import axios from 'axios'
import HeaderMenu from "./components/AppHeader";
import Footer from "./components/AppFooter";

// import APIUser from "./components/APIUser";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            //'authors': []
            // 'userapp': []
            'users': []
        }
    }
    //вызывается при монтировании компонента на страницу
    componentDidMount() {
        //асинхронный запрос
        axios.get('http://127.0.0.1:8000/api/userapp/')
            //если успешно, то ".then"
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => console.log(error))
        // const authors = [
        // const users = [
        //     {
        //         'first_name': 'Фёдор',
        //         'last_name': 'Достоевский',
        //         'email': 'geek1@gb.ru'
        //     },
        //     {
        //         'first_name': 'Александр',
        //         'last_name': 'Грин',
        //         'email': 'geek2@gb.ru'
        //     },
        // ]
        // с помощью метода this.setState меняем состояние компонента App и передаём данные
        // об пользователях
        // this.setState(
        //     {
        //         'users': users
        //     }
        // )
    }

    render() {
        return (
            <div>
                <HeaderMenu />
                <hr/>
                <APIUserList users={this.state.users}/>
                <hr/>
                <Footer />
            </div>
        )
    }
}

//Экспортируем наш компонент для использования в других модулях. Если открыть файл index.js,
// можно увидеть, что в нём используется компонент App.
export default App;
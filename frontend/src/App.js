import React from 'react';
import logo from './logo.svg';
import './App.css';
// import './css/bootstrap.min.css';
// import './css/sticky-footer-navbar.css';
import './components/AppHeader.css';
import APIUserList from './components/APIUser.js';
import axios from 'axios'
import HeaderMenu from "./components/AppHeader";
import Footer from "./components/AppFooter";
import ProjectList from "./components/Project";
import TodoList from "./components/Todo";
import UserProject from "./components/UserProject";
import NotFound404 from "./components/NotFound404"
// import TodoProject from "./components/TodoProject";
import {HashRouter, Route, Link, Switch, Redirect, BrowserRouter} from "react-router-dom";
import LoginForm from "./components/LoginForm";
import Cookies from 'universal-cookie';
// import './bootstrap/css/bootstrap.min.css'
// import './bootstrap/css/sticky-footer-navbar.css'

// import APIUser from "./components/APIUser";

// const NotFound404 = ({location}) => {
//     return (
//         <div>
//             <h1>Страница по адресу '{location.pathname}' не найдена</h1>
//         </div>
//     )
// }

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            //'authors': []
            // 'userapp': []
            'users': [],
            'projects': [],
            'todo': [],
            'token': '',
        }
    }

    is_authenticated() {
        //Метод "is_authenticated" определяет, авторизован пользователь или нет.
        // return this.state.token != ''
        return !!this.state.token
    }


    get_token_from_storage() {
        const cookie = new Cookies()
        // const token = cookie.get('token')
        //this.setState({'token': token})
        //если токен сохранён, он будет приложен к запросу get_data
        this.setState({'token': cookie.get('token')}, this.get_data)
    }

    get_headers() {
        let header = {
            'Content-type': 'application/json',
            'Accept' : 'application/json; version=v2'
        }
        const cookie = new Cookies()
        // cookies.set('token', response.data.token)
        //     //получаем токен
        //     console.log(cookies.get('token'))

        header['Authorization'] = 'Token ' + cookie.get('token')
        return header
    }

    get_data() {
        const headers = this.get_headers()
        // console.log(headers)

        //асинхронный запрос
        // axios.get('http://127.0.0.1:8000/api/users/')
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            //если успешно, то ".then"
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
                // }).catch(error => console.log(error))
            }).catch(error => {
            // при получении ошибки сбрасываем состояние
            this.setState({
                'users': []
            })
            console.log(error)
        })

        // axios.get('http://127.0.0.1:8000/api/projects/')
        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            //если успешно, то ".then"
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => {
            // при получении ошибки сбрасываем состояние
            this.setState({
                'projects': []
            })
            console.log(error)
        })

        // axios.get('http://127.0.0.1:8000/api/todo/')
        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            //если успешно, то ".then"
            .then(response => {
                const todo = response.data
                this.setState(
                    {
                        'todo': todo
                    }
                )
            }).catch(error => {
            // при получении ошибки сбрасываем состояние
            this.setState({
                'todo': []
            })
            console.log(error)
        })
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

    get_token(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/',
            {username: login, password: password})
            .then(response => {
                // console.log(response.data)
                // localStorage.setItem('token', response.data.token)
                const cookie = new Cookies()
                cookie.set('token', response.data.token)
                // //получаем токен
                // console.log(cookies.get('token'))
                this.setState({'token': response.data.token}, this.get_data)
            }).catch(error => alert('Неверный логин или пароль'))
    }

    logout() {
        const cookie = new Cookies()
        cookie.set('token', '')
        this.setState({'token': ''}, this.get_data)
    }

    //вызывается при монтировании компонента на страницу
    componentDidMount() {
        this.get_token_from_storage()

    }


    render() {
        return (
            <div className="App">
                {/*<HashRouter>*/}
                <BrowserRouter>
                    {/*<HeaderMenu/>*/}
                    <nav>
                        {/*{menu.map((value, index) => {*/}
                        {/*    return <div key={index}><a name={value}/></div>*/}
                        {/*})}*/}
                        <ul className="list-style">
                            <li><Link to='/'>Пользователи</Link></li>
                            <li><Link to='/projects'>Проекты</Link></li>
                            <li><Link to='/todo'>Заметки</Link></li>
                            {/*<li><Link to='/login'>Вход</Link></li>*/}
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Выход</button> :
                                    <Link to='/login'>Вход</Link>}
                            </li>
                            {/*<li>*/}
                            {/*    <button onClick={() => this.logout()}>Выход</button>*/}
                            {/*</li>*/}
                        </ul>
                    </nav>
                    <hr/>
                    <Switch>
                        <Route exact path='/' component={() => <APIUserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}
                                                                                    users={this.state.users}/>}/>
                        <Route exact path='/users/:id' component={() => <UserProject projects={this.state.projects}
                                                                                     users={this.state.users}/>}/>
                        {/*<Route exact path='/todo/:id' component={() => <TodoProject todos={this.state.todo}*/}
                        {/*                                                            projects={this.state.projects}/>}/>*/}
                        <Route exact path='/todo' component={() => <TodoList todos={this.state.todo}/>}/>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(login, password) => this.get_token(login, password)}/>}/>
                        <Redirect from='/users' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                    <hr/>
                    <Footer/>
                    {/*</HashRouter>*/}
                </BrowserRouter>
            </div>
        )
    }
}

//Экспортируем наш компонент для использования в других модулях. Если открыть файл index.js,
// можно увидеть, что в нём используется компонент App.
export default App;
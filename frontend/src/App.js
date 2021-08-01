import React from 'react';
import logo from './logo.svg';
import './App.css';
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
            'todo': []
        }
    }

    //вызывается при монтировании компонента на страницу
    componentDidMount() {
        //асинхронный запрос
        axios.get('http://127.0.0.1:8000/api/users/')
            //если успешно, то ".then"
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/')
            //если успешно, то ".then"
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/')
            //если успешно, то ".then"
            .then(response => {
                const todo = response.data
                this.setState(
                    {
                        'todo': todo
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
            <div className="App">
                {/*<HashRouter>*/}
                <BrowserRouter>
                    <HeaderMenu/>
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
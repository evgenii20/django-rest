import React from 'react'
import {Redirect} from "react-router-dom";


class LoginForm extends React.Component {
    // позволяет хранить состояние(логин и пароль) во время выполнения программы
    constructor(props) {
        super(props)
        this.state = {login: '', password: ''}
    }

    handleChange(event) {
        //Метод handleChange принимает в себя event — это событие, которое произойдёт при вводе данных в поля формы.
        // name="login"
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        // Метод handleSubmit будет выполняться при отправке формы.
        // console.log(this.state.login + ' ' + this.state.password)
        //вместо вывода в консоль логина и пароля вызовем метод get_token
        this.props.get_token(this.state.login, this.state.password)
        //event.preventDefault() отменит отправку формы. Это нужно, так как мы сами будем отправлять
        // запрос на сервер с помощью Axios.
        event.preventDefault()
    }

    render() {
        //Метод render отрисовывает компонент формы.
        return (
            //обработка события
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="login" placeholder="login" value={this.state.login}
                       onChange={(event) => this.handleChange(event)}/>
                <input type="password" name="password" placeholder="password" value={this.state.password}
                       onChange={(event) => this.handleChange(event)}/>
                <input type="submit" value="Login"/>
            </form>
        );
    }
}

export default LoginForm
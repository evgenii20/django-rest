import React from 'react'


class TodoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'todo': '',
            'textt': '',
            'project': [],
            // completed: false,
            'users': []
        }
    }

    handleChange(event) {
        // 1-обрабатывает только
        this.setState({
            [event.target.todo] : event.target.value,
            [event.target.textt] : event.target.value,
            // [event.target.is_active] : event.target.value
        })
    }

    handleUserChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'users' : []
            })
            return;
        }
        //пробегаем по массиву
        let users = []
        for(let i=0; i < event.target.selectedOptions.length; i++) {
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'users' : users
        })
    }

    handleSubmit(event) {
        this.props.createTodo(this.state.todo, this.state.textt, this.state.users);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <input type="text" name="todo" placeholder="name todo" value={this.state.name} onChange={(event)=>this.handleChange(event)} />
                <input type="text" name="textt" placeholder="text" value={this.state.text} onChange={(event)=>this.handleChange(event)} />
                <select multiple name="users" onChange={(event)=>this.handleUserChange(event)} >
                    {this.props.users.map((user) => <option value={user.id}>{user.first_name} {user.last_name}</option>)}
                </select>
                {/*<select name="users" onChange={(event)=>this.handleUserChange(event)} >*/}
                {/*    {this.props.users.map((user) => <option value={user.id}>{user.first_name} {user.last_name}</option>)}*/}
                {/*</select>*/}

                <input type="submit" value="Create" />
            </form>
        )
    }
}

// export default BookForm
export default TodoForm
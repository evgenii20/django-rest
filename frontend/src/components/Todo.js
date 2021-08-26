import React from 'react'
import Todo from "./Todo";
import {Link} from "react-router-dom";

const TodoItem = ({todo, users, deleteTodo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.todo}</td>
            <td>{todo.text}</td>
            <td>{todo.project}
                {/*<Link to={`todo/${todo.id}`}>{todo.project}</Link>*/}
            </td>
            <td><input
                type="checkbox"
                name="is_active"
                checked={todo.is_active.completed}
                onChange={() => console.log("Changed!")}
            />
                {/*{todo.is_active}*/}
            </td>
            <td>{todo.users}</td>
            <td>{todo.create_date}</td>
            <td>{todo.update_date}</td>
            {/*<td>*/}
            {/*    {todo.users.map((userID) => {*/}
            {/*        let user = users.find((user) => user.id == userID)*/}
            {/*        console.log('user', user)*/}
            {/*        if (user) {*/}

            {/*            return user.last_name*/}
            {/*        }*/}
            {/*    })}*/}
            {/*</td>*/}
            <td><button onClick={() => deleteTodo(todo.id)} type='button'>Delete</button></td>
        </tr>
    )
}

//Поднимаем на верх deleteTodo в App
const TodoList = ({todos, users, deleteTodo}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                TODO
            </th>
            <th>
                TEXT
            </th>
            <th>
                PROJECT
            </th>
            <th>
                IS_ACTIVE
            </th>
            <th>
                USERS
            </th>
            <th>
                CREATE_DATE
            </th>
            <th>
                UPDATE_DATE
            </th>
            {/*{users.map((user) => <AuthorItem author={user} />)}*/}
            {/*{todos.map((todo) => <TodoItem todo={todo}/>)}*/}
            {todos.map((todo) => <TodoItem todo={todo} users={users} deleteTodo={deleteTodo}/>)}
        </table>
    )
}

export default TodoList
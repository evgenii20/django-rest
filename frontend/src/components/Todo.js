import React from 'react'
import Todo from "./Todo";
import {Link} from "react-router-dom";

const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.id}
            </td>
            <td>
                {todo.todo}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.project}
                {/*<Link to={`todo/${todo.id}`}>{todo.project}</Link>*/}
            </td>
            <td>
                {todo.is_active}
            </td>
            <td>
                {todo.users}
            </td>
            <td>
                {todo.create_date}
            </td>
            <td>
                {todo.update_date}
            </td>
        </tr>
    )
}

const TodoList = ({todos}) => {
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
            {todos.map((todo) => <TodoItem todo={todo}/>)}
        </table>
    )
}

export default TodoList
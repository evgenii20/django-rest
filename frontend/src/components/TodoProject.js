import React from 'react'
import { useParams } from 'react-router-dom'


const TodoItem = ({todo, projects}) => {
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
            <td>
                {/*{project.users.name}*/}
                {/*{project.users}*/}
                {todo.projects.map((projectID) => {
                    return projects.find((project) => project.id == projectID).name
                }).join(', ')}
            </td>
        </tr>
    )
}

const TodoList = ({todos, projects}) => {
    let { id } = useParams();
    // let filtered_projects = projects.filter((project) => project.users.name === id)
    // let filtered_todos = todos.filter((todo) => todo.projects == todo.project)
    let filtered_todos = todos.filter((todo) => todo.projects.id == id)
    // let filtered_todos = todos.filter((todo) => todo.projects.includes(parseInt(id)))
    // let filtered_projects = projects.filter((project) => {
    //     console.log(id)
    //     console.log(project.users)
    //     console.log(project.users.id)
    //     return project.users.includes(parseInt(id));
    // })
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
            {/*{projects.map((project) => <ProjectItem project={project}/>)}*/}
            {filtered_todos.map((todo) => <TodoItem todo={todo} projects={projects}/>)}
        </table>
    )
}

export default TodoList
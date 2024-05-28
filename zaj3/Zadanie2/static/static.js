document.addEventListener("DOMContentLoaded", function () {
    const taskForm = document.getElementById("task-form");
    const taskInput = document.getElementById("task-input");
    const taskList = document.getElementById("task-list");

    taskForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const taskText = taskInput.value.trim();
        if (taskText !== "") {
            addTask(taskText);
            taskInput.value = "";
        }
    });

    taskList.addEventListener("click", function (event) {
        if (event.target.classList.contains("delete-task")) {
            const taskItem = event.target.closest("li");
            deleteTask(taskItem);
        } else if (event.target.classList.contains("edit-task")) {
            const taskItem = event.target.closest("li");
            editTask(taskItem);
        }
    });

    function addTask(taskText) {
        fetch("/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: `name=${encodeURIComponent(taskText)}`,
        })
        .then(response => response.text())
        .then(data => {
            const tempDiv = document.createElement("div");
            tempDiv.innerHTML = data;
            const newTask = tempDiv.querySelector(`li[data-id="${taskList.children.length}"]`);
            taskList.appendChild(newTask);
        });
    }

    function deleteTask(taskItem) {
        const taskId = taskItem.getAttribute("data-id");
        fetch(`/delete/${taskId}`, {
            method: "GET",
        })
        .then(response => response.text())
        .then(data => {
            taskItem.remove();
        });
    }

    function editTask(taskItem) {
        const taskId = taskItem.getAttribute("data-id");
        const taskText = taskItem.querySelector("span").innerText;
        const newTaskText = prompt("Edit your task:", taskText);
        if (newTaskText !== null && newTaskText.trim() !== "") {
            fetch(`/edit/${taskId}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: `name=${encodeURIComponent(newTaskText)}`,
            })
            .then(response => response.text())
            .then(data => {
                taskItem.querySelector("span").innerText = newTaskText;
            });
        }
    }
});
import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { TaskList, Task, IAuthResponse } from '../models/models';
import { promise } from 'protractor';

@Injectable({
  providedIn: 'root'
})

export class ProviderService extends MainService{

  constructor(http: HttpClient) {
    super(http);
 }
  getTaskLists(): Promise<TaskList[]>{

    return this.get('http://127.0.0.1:8000/api/task_lists/', {});
  }
  getTasks(id: number): Promise<Task[]>{
    return this.get(`http://127.0.0.1:8000/api/task_lists/${id}/tasks`, {});
  }

  updateTaskList(task_lists: TaskList): Promise<TaskList>{
    return this.put(`http://localhost:8000/api/task_lists/${task_lists.id}/`,{
      name: task_lists.name
    });
  }

  deleteTaskList(id: number) : Promise<any>{
     return this.delete(`http://localhost:8000/api/task_lists/${id}/`,{});
  }

  createTaskList(name: any) : Promise<TaskList>{
    return this.post(`http://localhost:8000/api/task_lists/`, {
      name: name
    });
  }

  auth(login: any, password: any) : Promise<IAuthResponse>{
    return this.post('http://localhost:8000/api/login/',{
      username: login,
      password: password
    });
  }

  logout() : Promise<any>{
    return this.post('http://localhost:8000/api/logout/', {

    });
  }
  
}

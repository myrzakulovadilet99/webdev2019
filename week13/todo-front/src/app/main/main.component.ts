import { Component, OnInit } from '@angular/core';
import { TaskList, Task } from '../shared/models/models';
import { ProviderService } from '../shared/services/provider.service';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public task_lists: TaskList[] = [];
  public tasks: Task[] = [];
  public loading = false;
  public name: any='';

  public logged = false;
  public login: any ='';
  public password: any ='';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if(token){
      this.logged = true;
    }
    if(this.logged){
      this.provider.getTaskLists().then(res =>{
        this.task_lists = res;
        setTimeout( () => {
          this.loading=true;
        }, 2000);
      });
    }
  }
  getListOfTasks(task_list: TaskList) {
    this.provider.getTasks(task_list.id).then(res => {
      this.tasks = res; 
    });
  }

  updateTaskList(c: TaskList){
    this.provider.updateTaskList(c).then(res =>{
      console.log(c.name+'updated');
    });
  }

  deleteTaskList(c: TaskList){
    this.provider.deleteTaskList(c.id).then(res => {
      console.log(c.name + 'deleted');
      this.provider.getTaskLists().then( res => {
        this.task_lists = res;
      })
    })
  }

  createTaskList(){
    if(this.name !== '') {
    this.provider.createTaskList(this.name).then( res => {
      this.name = '';
      this.task_lists.push(res);
      })
    }
  }

  auth() {
    console.log(this.login + " " + this.password);

    if (this.login !== '' && this.password !== '') {
      
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);

        console.log(res);

        this.logged = true;

        this.provider.getTaskLists().then(res => {
          this.task_lists = res;
          setTimeout(() => {
            this.loading = true;
          }, 2000);
        });

      });
    }
  }

  logout(){
    this.provider.logout().then(res => {
      localStorage.clear();
      this.logged=false;
    })
  }


}
import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ITasklist, ITask } from '../shared/models/model';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public task_lists: ITasklist[] = [];
  public loading = false;

  public tasks: ITask[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res=>{
      console.log('hjghgjh', res);
      this.task_lists = res;
      this.loading = true;
    });
  }

  getTasks(task_lists: ITasklist){
    this.provider.getTasks(task_lists).then(res=>{
      console.log(res);
      this.tasks = res;
    })
  }

}

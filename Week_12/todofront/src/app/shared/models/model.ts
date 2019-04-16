export interface ITasklist {
    id: number;
    name: string;
  }
  
  export interface ITask {
    id: number;
    name: string;
    status:string;
    created_at:string;
    due_on:string;
  }
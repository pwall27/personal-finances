import {Injectable} from '@angular/core';
import {HttpService} from "./http.service";
import {Transaction} from "../models/transaction.model";

@Injectable({
  providedIn: 'root'
})
export class TransactionService {

  constructor(private httpService: HttpService) {
  }

  list(ordering: string=null) {
    let url = "/transactions/";
    if(ordering){
      url += '?ordering=' + ordering;
    }
    return this.httpService.get(url);
  }

  create(transaction: Transaction) {
    return this.httpService.post(
      "/transactions/",
      transaction
    );
  }
}

import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CustomerSupport-card.component.html',
  styleUrls: ['./CustomerSupport-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CustomerSupport-card]': 'true'
  }
})

export class CustomerSupportCardComponent {


}
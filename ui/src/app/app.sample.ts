import { Component, OnInit } from "@angular/core";
import { RouterOutlet } from "@angular/router";

@Component({
  selector: "app-sample",
  standalone: true,
  imports: [RouterOutlet],
  template: `
    <p class="underline ...">The quick brown fox ...</p>
    <p class="overline ...">The quick brown fox ...</p>
    <p class="line-through ...">The quick brown fox ...</p>
    <p class="no-underline ...">The quick brown fox ...</p>
  `,
  styles: [],
})
export class SampleComponent implements OnInit {
  title = "user";

  ngOnInit(): void {}
}

import { Component, OnInit } from "@angular/core";
import { RouterOutlet } from "@angular/router";

@Component({
  selector: "app-root",
  standalone: true,
  imports: [RouterOutlet],
  template: `
    <h1 class="text-3xl font-bold underline text-cyan-400">
      Welcome to {{ title }}!
    </h1>

    <router-outlet />
  `,
  styles: [],
})
export class AppComponent implements OnInit {
  title = "user";

  ngOnInit(): void {}
}

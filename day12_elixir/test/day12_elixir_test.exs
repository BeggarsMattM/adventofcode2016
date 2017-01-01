defmodule Day12ElixirTest do
  use ExUnit.Case
  doctest Day12Elixir

  import Assembunny

  def registers do
    %{a: 0, b: 0, c: 0, d: 0}
  end

  test "assembunny copies x into y" do
    instruction = {:cpy, 41, :a}
    {registers, _} = registers |> process(instruction, 0)
    assert registers.a == 41
  end

  test "assembunny increments value of register" do
    instruction = {:inc, :a}
    {registers, _} = registers |> process(instruction, 0)
    assert registers.a == 1
  end

  test "assembunny decrements value of register" do
    instruction = {:dec, :a}
    {registers, _} = registers |> process(instruction, 0)
    assert registers.a == -1
  end

  test "assembunny handles group of instructions" do
    code = [{:cpy, 41, :a}, {:inc, :a}, {:inc, :a},
      {:dec, :a}, {:jnz, :a, 2}, {:dec, :a}]
    registers = registers |> execute(code, 0)
    assert registers.a == 42
  end

  test "assembunny copies values between registers" do
    code = [{:cpy, 41, :a}, {:cpy, :a, :b}, {:inc, :b}]
    registers = registers |> execute(code, 0)
    assert registers.a == 41
    assert registers.b == 42
  end

  test "assembunny can jnz based on value or register" do
    instruction = {:jnz, 1, 2}
    {registers, _} = registers |> process(instruction, 0)
    assert registers.a == 0
  end
end

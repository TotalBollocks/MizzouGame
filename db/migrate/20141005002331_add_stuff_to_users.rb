class AddStuffToUsers < ActiveRecord::Migration
  def up
    add_column :users, :kills, :integer, default: 0
    add_column :users, :study_time, :integer, default: 0
    add_column :users, :play_time, :integer, default: 0
    add_column :users, :last_played, :datetime
    change_column :users, :score, :integer, default: 0
  end
  
  def down
    remove_column :users, :kills
    remove_column :users, :study_time
    remove_column :users, :play_time
    remove_column :users, :last_played
    change_column :users, :score, :integer
  end
end
